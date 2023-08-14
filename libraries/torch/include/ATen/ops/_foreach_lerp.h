#pragma once

// @generated by torchgen/gen.py from Function.h

#include <ATen/Context.h>
#include <ATen/DeviceGuard.h>
#include <ATen/TensorUtils.h>
#include <ATen/TracerMode.h>
#include <ATen/core/Generator.h>
#include <ATen/core/Reduction.h>
#include <ATen/core/Tensor.h>
#include <c10/core/Scalar.h>
#include <c10/core/Storage.h>
#include <c10/core/TensorOptions.h>
#include <c10/util/Deprecated.h>
#include <c10/util/Optional.h>



#include <ATen/ops/_foreach_lerp_ops.h>

namespace at {


// aten::_foreach_lerp.List(Tensor[] self, Tensor[] tensors1, Tensor[] weights) -> Tensor[]
inline ::std::vector<at::Tensor> _foreach_lerp(at::TensorList self, at::TensorList tensors1, at::TensorList weights) {
    return at::_ops::_foreach_lerp_List::call(self, tensors1, weights);
}

// aten::_foreach_lerp_.List(Tensor(a!)[] self, Tensor[] tensors1, Tensor[] weights) -> ()
inline void _foreach_lerp_(at::TensorList self, at::TensorList tensors1, at::TensorList weights) {
    return at::_ops::_foreach_lerp__List::call(self, tensors1, weights);
}

// aten::_foreach_lerp.Scalar(Tensor[] self, Tensor[] tensors1, Scalar weight) -> Tensor[]
inline ::std::vector<at::Tensor> _foreach_lerp(at::TensorList self, at::TensorList tensors1, const at::Scalar & weight) {
    return at::_ops::_foreach_lerp_Scalar::call(self, tensors1, weight);
}

// aten::_foreach_lerp_.Scalar(Tensor(a!)[] self, Tensor[] tensors1, Scalar weight) -> ()
inline void _foreach_lerp_(at::TensorList self, at::TensorList tensors1, const at::Scalar & weight) {
    return at::_ops::_foreach_lerp__Scalar::call(self, tensors1, weight);
}

// aten::_foreach_lerp.List_out(Tensor[] self, Tensor[] tensors1, Tensor[] weights, *, Tensor(a!)[] out) -> ()
inline void _foreach_lerp_out(at::TensorList out, at::TensorList self, at::TensorList tensors1, at::TensorList weights) {
    return at::_ops::_foreach_lerp_List_out::call(self, tensors1, weights, out);
}
// aten::_foreach_lerp.List_out(Tensor[] self, Tensor[] tensors1, Tensor[] weights, *, Tensor(a!)[] out) -> ()
inline void _foreach_lerp_outf(at::TensorList self, at::TensorList tensors1, at::TensorList weights, at::TensorList out) {
    return at::_ops::_foreach_lerp_List_out::call(self, tensors1, weights, out);
}

// aten::_foreach_lerp.Scalar_out(Tensor[] self, Tensor[] tensors1, Scalar weight, *, Tensor(a!)[] out) -> ()
inline void _foreach_lerp_out(at::TensorList out, at::TensorList self, at::TensorList tensors1, const at::Scalar & weight) {
    return at::_ops::_foreach_lerp_Scalar_out::call(self, tensors1, weight, out);
}
// aten::_foreach_lerp.Scalar_out(Tensor[] self, Tensor[] tensors1, Scalar weight, *, Tensor(a!)[] out) -> ()
inline void _foreach_lerp_outf(at::TensorList self, at::TensorList tensors1, const at::Scalar & weight, at::TensorList out) {
    return at::_ops::_foreach_lerp_Scalar_out::call(self, tensors1, weight, out);
}

}
